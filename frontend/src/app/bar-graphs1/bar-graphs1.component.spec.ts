import { ComponentFixture, TestBed } from '@angular/core/testing';

import { BarGraphs1Component } from './bar-graphs1.component';

describe('BarGraphs1Component', () => {
  let component: BarGraphs1Component;
  let fixture: ComponentFixture<BarGraphs1Component>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ BarGraphs1Component ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(BarGraphs1Component);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
