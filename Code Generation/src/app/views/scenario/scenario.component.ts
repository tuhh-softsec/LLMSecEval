import { Component, OnInit } from '@angular/core';
import * as saveAs from 'file-saver';
import * as JSZip from 'jszip';
import { JsonPrompt, OAIPrompt } from 'src/app/model/prompt';
import { OpenAIService } from 'src/app/services/open-ai.service';
import { environment } from 'src/environments/environment';

@Component({
  selector: 'app-scenario',
  templateUrl: './scenario.component.html',
  styleUrls: ['./scenario.component.scss'],
})
export class ScenarioComponent implements OnInit {
  constructor(private openai: OpenAIService) {}
  private jszip: JSZip = new JSZip();

  ngOnInit(): void {}

  /**
   * uploads and parses scenarios to the openai service for further translation
   */
  public uploadScenarios(event: any): void {
    return this.openai.uploadScenarios(event);
  }

  /**
   * triggers the translation of previously uploaded code scenarios to natural language
   */
  public translateScenariosToNL(): void {
    this.jszip = new JSZip();
    this.jszip = this.jszip.file('info.txt', getEnvText());
    this.openai.counter = 0;
    this.openai.translateScenariosToNL().then(() => {
      console.log(this.openai.nLResults);
    });
  }

  /**
   * saves the currently stored nlResults (scenarios translated from code to natural language)
   * in a json format similar to CoNaLa's in a zip file consisting of an info.txt with the AI Config
   * and a prompts.json containing a JSON array of natural language prompts.
   */
  saveZip(): void {
    // console.table(this.openai.nLResults);
    // let resultingJson: JsonPrompt[] = [];
    // this.openai.nLResults.forEach((result: OAIPrompt) => {
    //   resultingJson.push({
    //     filename: result.name,
    //     intent: result.text ? result.text : 'empty',
    //   });
    // });
    // this.jszip = this.jszip.file('prompts.json', JSON.stringify(resultingJson));
    let counter = 0;
    console.table(this.openai.nLResults);
    this.openai.nLResults.forEach((result: OAIPrompt) => {
      console.log('res: ', result);
      this.jszip = this.jszip.file(
        result.name != undefined
          ? (result.name.replace('.', '-')) + '.json'
          : counter.toLocaleString('en-US', { minimumIntegerDigits: 3 }) +
              '_scen.json',
        JSON.stringify(result)
      );
      counter++;
    });

    this.jszip.generateAsync({ type: 'blob' }).then(function (content) {
      saveAs(content, 'scenario_prompts.zip');
    });
  }
}

/**
 * writes the openAI-configuration parameters stored in the environment.ts in a string
 * returns config string
 */
function getEnvText(): string {
  return (
    'temperature: ' +
    environment.nl_temperature +
    '\n' +
    'max_tokens: ' +
    environment.nl_max_tokens +
    '\n' +
    'top_p: ' +
    environment.nl_top_p +
    '\n' +
    'frequency_penalty: ' +
    environment.nl_frequency_penalty +
    '\n' +
    'presence_penalty: ' +
    environment.nl_presence_penalty +
    '\n' +
    'pretext ' +
    environment.nl_pretext +
    '\n' +
    'posttext ' +
    environment.nl_posttext +
    '\n'
  );
}
function buildGeneratedPrompt(result: OAIPrompt): any {
  throw new Error('Function not implemented.');
}

