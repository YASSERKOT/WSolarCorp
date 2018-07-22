import { Component } from '@angular/core';
import { Http, Response, Headers } from '@angular/http';
import { Observable } from 'rxjs';

import { map } from 'rxjs/operators';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'app';
/*   constructor(private http: Http) {}
  public getUsers() {
    const headers = new Headers();
    return this.http
           .get('http://127.0.0.1:8000/users', { headers: headers })
           .map(res => res.json().data);
  }
 */}
