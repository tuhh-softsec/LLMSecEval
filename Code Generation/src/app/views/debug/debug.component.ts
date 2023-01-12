import { Component, OnInit } from '@angular/core';
import { OAIResult } from 'src/app/model/result';
import { OpenAIService } from 'src/app/services/open-ai.service';
import * as JSZip from 'jszip';
import { saveAs } from 'file-saver';
import { environment } from 'src/environments/environment';
import { ProgrammingLanguage } from 'src/app/model/programming-language';
import { OAIPrompt } from 'src/app/model/prompt';
@Component({
  selector: 'app-debug',
  templateUrl: './debug.component.html',
  styleUrls: ['./debug.component.scss'],
})
export class DebugComponent implements OnInit {
  constructor(private openai: OpenAIService) {}

  private jszip: JSZip = new JSZip();
  ngOnInit(): void {}

  /**
   * uploads natural language prompt json file to openai-service for further to translation
   */
  uploadFile(event: any): void {
    this.openai.uploadDebugs(event);
  }

  /**
   * triggers the translation of the previously uploaded NLPrs to code snippets
   */
  generateDebugs(): void {
    this.jszip = new JSZip();
    this.jszip = this.jszip.file('info.txt', getEnvText());
    console.log("start");
    this.openai.generateDebugs().then(() => {
    });
  }

  /**
   * uses the code snippets from the translation and stores them in a .zip file,
   * including an info.txt file that contains the AI configuration parameters
   */
  saveZip(): void {
    let counter = 0;
    console.table(this.openai.results);
    this.openai.results.forEach((result: OAIResult) => {
      console.log('res: ', result);
      let lang: ProgrammingLanguage = ProgrammingLanguage.PYTHON;
      this.jszip = this.jszip.file(
        result.prompt.name != undefined
          ? result.prompt.name
          : counter.toLocaleString('en-US', { minimumIntegerDigits: 3 }) +
              '_scen.py',
        buildGeneratedCode(result.prompt, result.result)
      );
      counter++;
    });
    this.jszip.generateAsync({ type: 'blob' }).then(function (content) {
      saveAs(content, 'results.zip');
    });
  }
}
/**
 * returns a string containing the openai configuration parameters set in the environment.ts
 */
function getEnvText(): string {
  return (
    'temperature: ' +
    environment.temperature +
    '\n' +
    'max_tokens: ' +
    environment.max_tokens +
    '\n' +
    'top_p: ' +
    environment.top_p +
    '\n' +
    'frequency_penalty: ' +
    environment.frequency_penalty +
    '\n' +
    'presence_penalty: ' +
    environment.presence_penalty +
    '\n' +
    'pretext: ' +
    environment.pretext +
    '\n' +
    'posttext: ' +
    environment.posttext
  );
}
function buildGeneratedCode(
  prompt: OAIPrompt,
  result: string | undefined
): string {
  let gen: string = '';
  let delimit: string = '';
  switch(prompt.language) {
    case ProgrammingLanguage.C:
      delimit = '\n//';
      break;
    case ProgrammingLanguage.PYTHON:
      delimit = '\n#'
  }
  let genArray: string = prompt.text ? prompt.text.split('\n').join(delimit) : (delimit +  'empty');
  gen = genArray + '\n' + (result ? result : 'empty');
  return gen;
}
