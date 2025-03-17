import { Component, OnInit } from '@angular/core';
import { SafeValue } from '@angular/platform-browser';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {

  currentYear!: number;

  ngOnInit() {
    this.currentYear = new Date().getFullYear();
  }

  title = 'AngularQRCodeGenerator';
  qrdata = '';
  qrCodeDownloadLink: SafeValue = '';

  onChange(url: any) {
    this.qrCodeDownloadLink = url;
  }
}
