import { Component, OnInit } from '@angular/core';
import { Http, Response, Headers } from '@angular/http';
import { Observable } from 'rxjs';

import * as L from 'leaflet';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
/*
export class AppComponent {
  title = 'app';
   constructor(private http: Http) {}
  public getUsers() {
    const headers = new Headers();
    return this.http
           .get('http://127.0.0.1:8000/users', { headers: headers })
           .map(res => res.json().data);
  }
}
*/

// Implémenter OnInit
export class AppComponent implements OnInit {

  // Fonction d'initialisation du composant.
  ngOnInit() {
    // Déclaration de la carte avec les coordonnées du centre et le niveau de zoom.
    const myfrugalmap = L.map('frugalmap').setView([50.6311634, 3.0599573], 12);

    L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
      attribution: 'Frugal Map'
    }).addTo(myfrugalmap);
  }
}
