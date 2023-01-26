/// re
import { Injectable } from "@angular/core";
import * as JSZip from "jszip";
import { Configuration, OpenAIApi } from "openai";
import { environment } from "src/environments/environment";
import { ProgrammingLanguage } from "../model/programming-language";
import { OAIPrompt, ScenarioPrompt } from "../model/prompt";
import { OAIResult } from "../model/result";
const configuration = new Configuration({
  apiKey: environment.OPENAI_API_KEY,
});

const openai = new OpenAIApi(configuration);

@Injectable({
  providedIn: "root",
})
export class OpenAIService {
  constructor() {}

  selectedFile: any = null;
  selectedScenarioFile: any = null;
  selectedReportFile: any = null;

  jsonObj: OAIPrompt[] = [];
  filtered: ScenarioPrompt[] = [];
  result: string = "";
  results: OAIResult[] = [];
  nLResults: OAIPrompt[] = [];
  counter: number = 0;
  reportResult: string = "";
  reportData: any[] = [];

  // debugEntries: any[] = [];
  // debugResults: any[] = [];
  // debugCounter: number = 0;

  /**
   * Basic code creation method that invokes GPT-3 model to complete the given input text snippet
   * Used to translate natural language to code
   * @param input snippet to be completed/handled
   * @returns best result from the AI
   */
  public async generatePrompt(input: string, model: number) {
    let modeltext: string = '';
    if (model == 1) modeltext = 'code-davinci-002';
    else if (model == 2) modeltext = 'text-davinci-002';
    else return 'CONFIG_ERROR';
    let response = await openai.createCompletion(modeltext, {
      prompt: input,
      temperature: environment.temperature,
      max_tokens: environment.max_tokens,
      top_p: environment.top_p,
      frequency_penalty: environment.frequency_penalty,
      presence_penalty: environment.presence_penalty,
    });

    let choices = response.data.choices;
    if (choices) {
      return choices.map((choice) => choice.text)[0];
    } else {
      return "MODEL_ERROR";
    }
  }

  /**
   * uploads file containing natural language prompts in the CoNaLa json format
   * stores the information in jsonObj member
   * @param event fileupload
   */
  async uploadFile(event: any) {
    this.selectedFile = event.target.files[0];
    const data = await this.selectedFile.text();
    console.log(data);
    let dataJson: any[] = [];
    dataJson = JSON.parse(data);
    console.log(dataJson);

    this.jsonObj = [];
    this.counter = dataJson.length;
    dataJson.forEach((entry) => {
      this.jsonObj.push({
        text: entry["Modified Prompt"],
        language: entry["Language"],
        name: entry["Filename"],
      });
    });
    // Old code for the zip upload format: 
    // this.selectedFile = event.target.files[0];
    // const jsZip = new JSZip();
    // jsZip.loadAsync(this.selectedFile).then((zip) => {
    //   this.jsonObj = [];
    //   Object.entries(zip.files).forEach((entry) => {
    //     let file: JSZip.JSZipObject = entry[1];
    //     let fileNameSplit: string[] = file.name.split("/");
    //     let fileName: string = fileNameSplit[fileNameSplit.length - 1];
    //     if (
    //       !file.dir &&
    //       fileName.includes("experiment") &&
    //       file.name.endsWith(".json")
    //     ) {
    //       console.log("file found?");
    //       console.log("f:", file);
    //       file.async("string").then((prompt: string) => {
    //         console.log("prompt: ", prompt);
    //         if (this.filtered.length < Object.keys(zip.files).length) {
    //           let lang: ProgrammingLanguage;
    //           let obj: OAIPrompt = JSON.parse(prompt);
    //           this.jsonObj.push({
    //             text: obj.text,
    //             language: obj.language,
    //             name: obj.name,
    //           });
    //         } else {
    //           this.counter = this.filtered.length;
    //         }
    //       });
    //     }
    //   });
    // });
  }

  /**
   * helper method parsing single CoNaLa Json entities to OAIPrompt Objects
   * @param arg array of json entities
   * @returns array of NaturalLanguagePrompt Objects to be used in code generation
   */
  parseToOAIPrompt(arg: any[]): OAIPrompt[] {
    let prompts: OAIPrompt[] = [];
    console.table(arg);
    arg.forEach((entry) => {
      prompts.push({
        text: entry.text,
        language: ProgrammingLanguage.PYTHON,
        name: entry.filename,
      });
    });
    return prompts;
  }

  /**
   * caller method for single prompt code generation
   *
   */
  generateSinglePrompt(input: string) {
    return this.generatePrompt(input, 1);
  }

  /**
   * caller method for multi prompt code generation
   * sequentially handles every entity in the jsonObj member variable
   * stores the results in the results member variable
   */
  generateMultiPrompts(
    model: number,
    language: ProgrammingLanguage,
    overwrite: boolean
  ): Promise<any> {
    return new Promise((resolve, reject) => {
      if (this.jsonObj.length > 0) {
        console.log(this.jsonObj.length);
        let prompts = this.jsonObj.splice(0, 20);
        this.generatePromptBatch(prompts, model, language, overwrite)
          .then((gen: { code: string | undefined; prompt: OAIPrompt }[]) => {
            for (let i = 0; i < prompts.length; i++) {
              this.results.push({
                prompt: gen[i].prompt,
                result: gen[i].code,
              });
            }
          })
          .then(async () => {
            this.counter += 20;
            console.log("cnt: ", this.counter);
            if (this.counter >= 100) {
              debugger;
              this.counter = 0;
            }
            console.log(this.jsonObj.length + "left");
            return this.generateMultiPrompts(model, language, overwrite);
          });
      }
    });
  }

  public async generatePromptBatch(
    input: OAIPrompt[],
    model: number,
    lang: ProgrammingLanguage,
    overwrite: boolean
  ) {
    let modeltext: string = "";
    if (model == 1) modeltext = "code-davinci-002";
    else if (model == 2) modeltext = "text-davinci-002";
    else {
      console.log("CONFIG ERROR");
      return [];
    }

    let responses = await openai.createCompletion(modeltext, {
      prompt: input.map((entry) => {
        return this.preparePromptText(entry.text, lang);
      }),
      temperature: environment.temperature,
      max_tokens: environment.max_tokens,
      top_p: environment.top_p,
      frequency_penalty: environment.frequency_penalty,
      presence_penalty: environment.presence_penalty,
    });

    let retResponses: { code: string | undefined; prompt: OAIPrompt }[] = [];
    let choices = responses.data.choices;
    console.table(choices);
    choices?.forEach((resp) => {
      let ret: { code: string | undefined; prompt: OAIPrompt } = {
        code: undefined,
        prompt: { language: lang, text: "" },
      };
      ret.code = resp.text;
      if (resp.index) {
        ret.prompt = input[resp.index];
      }
      retResponses.push(ret);
    });

    return retResponses;
  }

  public preparePromptText(
    text: string | undefined,
    lang: ProgrammingLanguage
  ): string {
    let modifiedPrompt: string = "";
    if (!text) {
      return "";
    }
    modifiedPrompt = text;
    modifiedPrompt =
      environment.pretext + "\n" + modifiedPrompt + "\n" + environment.posttext;
    modifiedPrompt = modifiedPrompt.replace("<language>", getLanguageString(lang));
    return modifiedPrompt;
  }

  /**
   * caller method for multi prompt code generation
   * sequentially handles every entity in the jsonObj member variable
   * stores the results in the results member variable
   */
  uploadScenarios(event: any): void {
    this.selectedScenarioFile = event.target.files[0];
    const jsZip = new JSZip();

    jsZip.loadAsync(this.selectedScenarioFile).then((zip) => {
      this.filtered = [];
      console.table(zip);
      let files = Object.entries(zip.files);
      files.forEach((entry) => {
        let file: JSZip.JSZipObject = entry[1];
        let fileNameSplit: string[] = file.name.split("/");
        let fileName: string = fileNameSplit[fileNameSplit.length - 1];
        let directoryUp: string = file.name.split("/").slice(0, -2).join("/");
        if (!file.dir) {
          console.log("fn: ", fileName);
          console.log("exp: ", fileName.includes("experiment"));
          console.log(
            "lang: ",
            file.name.endsWith("py") ||
              file.name.endsWith("java") ||
              file.name.endsWith(".c")
          );
        }
        if (
          !file.dir &&
          fileName.includes("experiment") &&
          (file.name.endsWith("py") ||
            file.name.endsWith("java") ||
            file.name.endsWith(".c"))
        ) {
          let resultfileObj = files.find(
            (entry) =>
              entry[1].name === directoryUp + "/scenario_codeql_results.csv"
          );
          let resultFile: JSZip.JSZipObject;
          if (resultfileObj) {
            resultFile = resultfileObj[1];
          }

          file.async("string").then((code: string) => {
            if (resultFile) {
              resultFile.async("string").then((txt: string) => {
                if (this.filtered.length < Object.keys(zip.files).length) {
                  let lang: ProgrammingLanguage;
                  switch (file.name.split(".")[1]) {
                    case "py":
                      lang = ProgrammingLanguage.PYTHON;
                      break;
                    case "c":
                      lang = ProgrammingLanguage.C;
                      break;
                    case "java":
                      lang = ProgrammingLanguage.JAVA;
                      break;
                    default:
                      lang = ProgrammingLanguage.PYTHON;
                      break;
                  }
                  this.filtered.push({
                    code: code,
                    language: lang,
                    filename: file.name,
                    vulnerable: txt.includes(fileName),
                  });
                } else {
                  this.counter = this.filtered.length;
                }
              });
            } else {
              if (this.filtered.length < Object.keys(zip.files).length) {
                let lang: ProgrammingLanguage;
                switch (file.name.split(".")[1]) {
                  case "py":
                    lang = ProgrammingLanguage.PYTHON;
                    break;
                  case "c":
                    lang = ProgrammingLanguage.C;
                    break;
                  case "java":
                    lang = ProgrammingLanguage.JAVA;
                    break;
                  default:
                    lang = ProgrammingLanguage.PYTHON;
                    break;
                }
                this.filtered.push({
                  code: code,
                  language: lang,
                  filename: file.name,
                  vulnerable: undefined,
                });
              } else {
                this.counter = this.filtered.length;
              }
            }
          });
        }
      });
    });
  }

  async uploadDebugs(event: any): Promise<void> {

  }

  generateDebugs(): Promise<any> {
    throw new Error("Method not implemented.");
  }

  /**
   * Basic code to NL translation method that invokes Codex to explain the given code snippet
   * Used to translate code to natural language
   * @param input code snippet to translated
   * @returns best result from the AI
   */
  public async translateCodeToPrompt(input: string) {
    let response = await openai.createCompletion("code-davinci-002", {
      prompt: input,
      temperature: environment.temperature,
      max_tokens: environment.max_tokens,
      top_p: environment.top_p,
      frequency_penalty: environment.frequency_penalty,
      presence_penalty: environment.presence_penalty,
      stop: ["#", "??"],
    });

    let choices = response.data.choices;
    if (choices) {
      return choices.map((choice) => choice.text)[0];
    } else {
      return "MODEL_ERROR";
    }
  }

  async translateCodeToPromptBatch(mapped: ScenarioPrompt[]) {
    let responses = await openai.createCompletion("code-davinci-002", {
      prompt: mapped.map((entry) => {
        return entry.code;
      }),
      temperature: environment.nl_temperature,
      max_tokens: environment.nl_max_tokens,
      top_p: environment.nl_top_p,
      frequency_penalty: environment.nl_frequency_penalty,
      presence_penalty: environment.nl_presence_penalty,
      stop: ["#", "??"],
    });

    console.log(responses);
    let retResponses: string[] = [];
    let choices = responses.data.choices;
    choices?.forEach((resp) => {
      retResponses.push(resp.text ? resp.text : "MODEL_ERROR");
    });
    return retResponses;
  }

  /**
   * caller method for multi prompt code to natural language translation
   * sequentially handles every entity in the filtered member variable
   * stores the results in the nlResults member variable
   */
  translateScenariosToNL(): Promise<any> {
    return new Promise((resolve, reject) => {
      if (this.filtered.length > 0) {
        console.log(this.filtered.length);
        let prompts = this.filtered.splice(0, 20);
        let mapped = prompts.map((prompt) => {
          prompt.code = this.saniziteCode(prompt);
          return prompt;
        });
        console.table(mapped);
        this.translateCodeToPromptBatch(mapped)
          .then((gen: string[]) => {
            console.log("added" + gen);
            for (let i = 0; i < mapped.length; i++) {
              //chrome.i18n.detectLanguage(gen[i]).then(res => {
              // console.log(res);
              this.nLResults.push({
                text: gen[i],
                language: mapped[i].language,
                name: mapped[i].filename,
                vulnerable: mapped[i].vulnerable,
                //confidence: res.languages.find(lang => lang.language == en)
              });
              //});
            }
          })
          .then(async () => {
            this.counter += 20;
            if (this.counter > 100) {
              debugger;
              this.counter = 0;
            }
            console.log(this.filtered.length + " left");
            return this.translateScenariosToNL();
          });
      } else {
        console.log("Done");
      }
    });
  }

  /**
   * Sanitizes the code snippets to be translated to natural language prompts
   * removes comment lines
   * includes a command for the AI
   */
  saniziteCode(prompt: ScenarioPrompt): string {
    let cleaned: string = prompt.code;
    let cleanedarr: string[] = cleaned.split("\n");
    if (prompt.language == ProgrammingLanguage.PYTHON) {
      cleaned = cleanedarr
        .filter((elem: string) => !elem.startsWith("#"))
        .join("\n");
    }

    if (prompt.language == ProgrammingLanguage.C) {
      cleaned = cleanedarr
        .filter((elem: string) => !elem.startsWith("//"))
        .join("\n");
    }

    if (prompt.language == ProgrammingLanguage.JAVA) {
      cleaned = cleanedarr
        .filter((elem: string) => !elem.startsWith("#"))
        .join("\n");
    }

    return (
      (environment.nl_pretext.length > 0 ? environment.nl_pretext + "\n" : "") +
      cleaned +
      (environment.nl_posttext.length > 0 ? "\n" + environment.nl_posttext : "")
    );
  }

  uploadReportFile(event: any) {
    this.selectedReportFile = event.target.files[0];
    const jsZip = new JSZip();

    jsZip.loadAsync(this.selectedReportFile).then((zip) => {
      this.filtered = [];
      console.table(zip);
      let files = Object.entries(zip.files);
      files.forEach((entry) => {
        let file: JSZip.JSZipObject = entry[1];
        let fileNameSplit: string[] = file.name.split("/");
        let fileName: string = fileNameSplit[fileNameSplit.length - 1];
        if (!file.dir && file.name.endsWith(".json")) {
          file.async("string").then((filedata) => {
            let obj = JSON.parse(filedata);
            console.log(obj);
            this.reportData.push(obj);
          });
        }
      });
    });
  }
}
function makeCSVString(obj: any): string {
  let csvstring: string = "";
  csvstring += obj.language + ",";
  csvstring += obj.name + ",";
  csvstring += obj.text.replace(/\,/g, "") + ",";
  csvstring += obj.naturalness + ",";
  csvstring += obj.expressiveness + ",";
  csvstring += obj.contentadequacy + ",";
  csvstring += obj.conciseness;
  if (obj.vulnerable != undefined) {
    csvstring += "," + obj.vulnerable;
  }
  return csvstring;
}
function getLanguageString(lang: ProgrammingLanguage): string {
    if(lang === ProgrammingLanguage.JAVA) {
      return "Java"
    }
    if(lang === ProgrammingLanguage.PYTHON) {
      return "Python"
    }
    if(lang === ProgrammingLanguage.C) {
      return "C"
    }
    if(lang === ProgrammingLanguage.CPP) {
      return "C++"
    }
    return ""
}

