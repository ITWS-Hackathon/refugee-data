import { BackendService } from '../backend.service';
import { Component, OnInit, ViewChild } from '@angular/core';
import { ChartConfiguration, ChartData, ChartEvent, ChartType } from 'chart.js';
import { BaseChartDirective } from 'ng2-charts';


import DataLabelsPlugin from 'chartjs-plugin-datalabels';

@Component({
  selector: 'app-graph',
  templateUrl: './graph.component.html',
  styleUrls: ['./graph.component.css']
})
export class GraphComponent implements OnInit {
  location: Array<string> = [];
  value: Array<number> = [];
  year: Array<number> = [];

  options: any;
  constructor(private backend: BackendService) { }

  async getData() {

  }

  parseData(data: object) {
    let jsonData = JSON.parse(JSON.stringify(data));
    console.log(jsonData);
    // console.log(jsonData['Location'])
    // console.log(jsonData['Value'])
    // console.log(jsonData['Year'])
    // json to array now
    for (let index in jsonData['Location']) {
      this.location.push(jsonData['Location'][index]);
      this.value.push(jsonData['Value'][index]);
      this.year.push(jsonData['Value'][index]);
    }
    console.log(this.location)
    console.log(this.value)   
    console.log(this.year) 
  }

  ngOnInit(): void {
    this.backend.getRequest('http://localhost:3000/continents').subscribe(data => {
      console.log(data)
        this.parseData(data!);
        const xAxisData = [];
        const datas: Array<Array<number>> = [];
        const names: Array<string> = [];

        for (let i = 0; i < this.location.length/6; i++) {
          let temp: Array<number> = []
          names.push(this.location[i*6]);

          for (let j = 0; j < 6; j++) {
            // 6 of these has something
            temp.push(this.value[i*6+j])
          }
          datas.push(temp)
        }
        let series_info = [];
        for (let i = 0; i < this.location.length/6; i++) {
          series_info.push({
            name: names[i],
            type: 'bar',
            data: datas[i],
            animationDelay: (idx: number) => idx * 10 + i*100,
          })
        }

        this.options = {
          // title: {
          //   text: "Number of international students by Continent of origin",
          //   subtext: "2015-2020",
          //   verticalAlign: top,

          // },
          legend: {
            data: this.location,
            align: 'left',
          },
          tooltip: {},
          xAxis: {
            data: [2015, 2016, 2017, 2018, 2019, 2020],
            silent: false,
            splitLine: {
              show: false,
            },
          },
          yAxis: {},
          series: series_info,
          animationEasing: 'elasticOut',
          animationDelayUpdate: (idx: number) => idx * 5,
        };
    })

  }

}
