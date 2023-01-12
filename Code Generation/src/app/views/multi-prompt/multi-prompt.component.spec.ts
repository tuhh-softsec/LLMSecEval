import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MultiPromptComponent } from './multi-prompt.component';

describe('MultiPromptComponent', () => {
  let component: MultiPromptComponent;
  let fixture: ComponentFixture<MultiPromptComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ MultiPromptComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(MultiPromptComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
