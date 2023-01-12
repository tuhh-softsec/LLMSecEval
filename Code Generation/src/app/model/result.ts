import { ProgrammingLanguage } from "./programming-language";
import { OAIPrompt } from "./prompt";

export interface OAIResult {
  prompt: OAIPrompt;
  result: string | undefined;
  lang?: ProgrammingLanguage;
}
