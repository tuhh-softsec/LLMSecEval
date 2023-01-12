import { Component, OnInit } from '@angular/core';
import { OpenAIService } from 'src/app/services/open-ai.service';

@Component({
  selector: 'app-single-prompt',
  templateUrl: './single-prompt.component.html',
  styleUrls: ['./single-prompt.component.scss'],
})
export class SinglePromptComponent implements OnInit {
  public results: string[] = [];

  constructor(private openai: OpenAIService) {}

  ngOnInit(): void {}

  public generateSinglePrompt(prompt: string): void {
    this.openai.generateSinglePrompt(prompt).then((choices) => {
      if (choices == 'MODEL_ERROR' || choices == undefined) {
        this.results[0] = 'ERROR';
      } else {
        this.results.push(choices);
      }
    });
  }
}
