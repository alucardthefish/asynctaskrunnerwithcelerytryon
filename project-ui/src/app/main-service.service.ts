import { Injectable } from '@angular/core';
import { HttpClient } from "@angular/common/http"
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class MainServiceService {
  private apiUrl = "http://localhost:8010"

  constructor(private http: HttpClient) { }

  public getUsers(): Observable<any> {
    return this.http.get<any>(`${this.apiUrl}/user/`);
  }
}
