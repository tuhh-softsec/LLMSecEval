import { ProgrammingLanguage } from "./programming-language";

export interface OAIPrompt {
  text: string | undefined;
  language: ProgrammingLanguage;
  name?: string;
  confidence?: number;
  vulnerable?: boolean;
}


export interface ScenarioPrompt {
  code: string;
  language: ProgrammingLanguage;
  filename?: string;
  vulnerable?: boolean;
}

export interface JsonPrompt {
  intent: string;
  filename?: string;
}
