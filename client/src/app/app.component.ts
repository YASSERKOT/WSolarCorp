import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
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

  constructor(private http: HttpClient) {}

  // Fonction d'initialisation du composant.
  ngOnInit() {
    // Déclaration de la carte avec les coordonnées du centre et le niveau de zoom.
    const myfrugalmap = L.map('frugalmap').setView([7.110228, 18.9994998], 3);

    L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
      attribution: 'Frugal Map'
    }).addTo(myfrugalmap);
    const myIcon = L.icon({
      iconUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.2.0/images/marker-icon.png'
    });
    function whenClicked(e) {
      console.log(e);
      L.marker([e.latlng.lat, e.latlng.lng], {icon: myIcon}).bindPopup(e.layerPoint.x + ' ; ' + e.layerPoint.y).addTo(myfrugalmap).openPopup();
    }
    function onEachFeature(feature, layer) {
      // does this feature have a property named popupContent?
      layer.on({
        click: whenClicked
      });
      if (feature.properties.name == 'Tunisia') {
        layer.setStyle({fillColor : 'red'});
      }
    }
     this.http.get('http://localhost:4200/regions/regions/').subscribe((data: any) => {
      L.geoJSON(data, {
        onEachFeature: onEachFeature
      }).addTo(myfrugalmap);
      /*
      // This part of code concerns the processing of the ordinary json passed as rest response.
      data.features.forEach(country => {
        L.marker([country.geometry.coordinates[0][0][0], country.geometry.coordinates[0][0][1]], {icon: myIcon}).addTo(myfrugalmap);
      });*/
    });

  }

}

