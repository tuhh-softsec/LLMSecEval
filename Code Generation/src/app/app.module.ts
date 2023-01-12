import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { SinglePromptComponent } from './views/single-prompt/single-prompt.component';
import { MultiPromptComponent } from './views/multi-prompt/multi-prompt.component';
import { ScenarioComponent } from './views/scenario/scenario.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MatTabsModule } from '@angular/material/tabs';
import { MatDialogModule } from '@angular/material/dialog';
import {MatProgressSpinnerModule} from '@angular/material/progress-spinner';
import { DebugComponent } from './views/debug/debug.component';
import { ReportComponent } from './views/report/report.component';
import { MatRadioModule} from '@angular/material/radio'
import { FormsModule } from '@angular/forms';

@NgModule({
  declarations: [
    AppComponent,
    SinglePromptComponent,
    MultiPromptComponent,
    ScenarioComponent,
    DebugComponent,
    ReportComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    MatTabsModule,
    MatDialogModule,
    MatProgressSpinnerModule,
    MatRadioModule,
    FormsModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
