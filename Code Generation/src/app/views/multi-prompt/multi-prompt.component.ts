import { Component, OnInit } from '@angular/core';
import { OAIResult } from 'src/app/model/result';
import { OpenAIService } from 'src/app/services/open-ai.service';
import * as JSZip from 'jszip';
import { saveAs } from 'file-saver';
import { environment } from 'src/environments/environment';
import { ProgrammingLanguage } from 'src/app/model/programming-language';
import { OAIPrompt } from 'src/app/model/prompt';
@Component({
  selector: 'app-multi-prompt',
  templateUrl: './multi-prompt.component.html',
  styleUrls: ['./multi-prompt.component.scss'],
})
export class MultiPromptComponent implements OnInit {
  constructor(private openai: OpenAIService) {}
  public languageEnum = ProgrammingLanguage;
  private jszip: JSZip = new JSZip();
  public generationModel: number = 0;
  public languageOverwrite: boolean = false;
  public generationLanguage: ProgrammingLanguage = ProgrammingLanguage.PYTHON;

  public prePrompt: string = environment.pretext;
  public postPrompt: string = environment.posttext;
  ngOnInit(): void {}

  /**
   * uploads natural language prompt json file to openai-service for further to translation
   */
  uploadFile(event: any): void {
    this.openai.uploadFile(event);
  }

  /**
   * triggers the translation of the previously uploaded NLPrs to code snippets
   */
  generateMultiPrompts(): void {
    this.jszip = new JSZip();
    this.jszip = this.jszip.file('info.txt', getEnvText());
    console.log('start');
    this.openai
      .generateMultiPrompts(
        this.generationModel,
        this.generationLanguage,
        this.languageOverwrite
      )
      .then(() => {
        console.log(this.openai.results);
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
      let lang: ProgrammingLanguage = this.generationLanguage;
      let filenamestring: string =
        result.prompt.name != undefined
          ? result.prompt.name
          : counter.toLocaleString('en-US', { minimumIntegerDigits: 3 }) +
            '_scen.helper'; // helper fileending because its removed in the next step for all non helper files.
      if(filenamestring.includes('_scen.helper')) {
        console.table(result);
      }
      let filenamestringarray = filenamestring.split('.');
      filenamestringarray = filenamestringarray.slice(0, -1);
      filenamestring = filenamestringarray[0] + "." + getFileNameEnding(lang);
      this.jszip = this.jszip.file(
        filenamestring,
        buildGeneratedCode(result.prompt, result.result, this.generationLanguage)
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
  result: string | undefined,
  lang: ProgrammingLanguage
): string {
  //todo: support for the other languages as well
  let gen: string = '';
  let delimit: string = '';
  switch (lang) {
    case ProgrammingLanguage.C:
      delimit = '\n//';
      break;
    case ProgrammingLanguage.PYTHON:
      console.log("pydelimit");
      delimit = '\n#';
      break;
    case ProgrammingLanguage.JAVA:
      delimit = '\n//';
      break;
    case ProgrammingLanguage.CPP:
      delimit = '\n//'
      break;
    case ProgrammingLanguage.TS:
      delimit = '\n//'
      break;
    }
  let genArray: string = prompt.text
    ? prompt.text.split('\n').join(delimit)
    : delimit + 'empty';
  gen = genArray + '\n' + (result ? result : 'empty');
  return gen;
}
function getFileNameEnding(lang: ProgrammingLanguage) {
  if(lang === ProgrammingLanguage.JAVA) {
    return "java"
  }
  if(lang === ProgrammingLanguage.PYTHON) {
    return "py"
  }
  if(lang === ProgrammingLanguage.C) {
    return "c"
  }
  if(lang === ProgrammingLanguage.CPP) {
    return "cpp"
  }
  return "txt"
}

