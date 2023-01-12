import { stringify } from '@angular/compiler/src/util';
import { Component, OnInit } from '@angular/core';
import { writeToPath } from 'fast-csv';
import * as saveAs from 'file-saver';
import { OpenAIService } from 'src/app/services/open-ai.service';

@Component({
  selector: 'app-report',
  templateUrl: './report.component.html',
  styleUrls: ['./report.component.scss'],
})
export class ReportComponent implements OnInit {
  constructor(private openai: OpenAIService) {}

  ngOnInit(): void {}

  /**
   * uploads natural language prompt json file to openai-service for further to translation
   */
  uploadReportFile(event: any): void {
    this.openai.uploadReportFile(event);
  }

  /**
   * uses the code snippets from the translation and stores them in a .zip file,
   * including an info.txt file that contains the AI configuration parameters
   */
  saveReport(): void {
    console.table(this.openai.reportData);
    const regex = new RegExp(/\\n|\n|\,/g)
    let helper: string[] = [];
    this.openai.reportData.forEach((entry) => {
      helper.push(JSON.stringify(entry).replace(regex, ''));
    });
    console.log('after');
    console.table(helper);
    this.openai.reportResult = JSON.stringify(helper);

    var blob = new Blob([this.openai.reportResult], { type: 'text/json' });
    saveAs(blob, 'report.json');
  }
}
