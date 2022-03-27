import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { RouterModule } from '@angular/router';
import { AppComponent } from './app.component';
import { NavbarComponent } from './navbar/navbar.component';
import { FooterComponent } from './footer/footer.component';
import { DescComponent } from './desc/desc.component';
import { ResourcesComponent } from './resources/resources.component';
import { BarGraphs1Component } from './bar-graphs1/bar-graphs1.component';
import { WordcloudComponent } from './wordcloud/wordcloud.component';

@NgModule({
  declarations: [
    AppComponent,
    NavbarComponent,
    FooterComponent,
    DescComponent,
    ResourcesComponent,
    BarGraphs1Component,
    WordcloudComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    RouterModule.forRoot([
      {path: 'resources', component: ResourcesComponent},
    ]),
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
