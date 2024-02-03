import { Component, OnInit } from '@angular/core';
import { MainServiceService } from './main-service.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  title = 'FastAPI With Celery';
  users: any[];

  constructor(private myService: MainServiceService) {}
  ngOnInit(): void {
    this.myService.getUsers().subscribe(data => {
      this.users = data;
      console.log("users: ", data);
    });
  }


}
