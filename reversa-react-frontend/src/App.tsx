import React from 'react';
import logo from './assets/logo.svg';
import meeting_room from "./assets/meeting_room.jpg"

import { Room } from './entities/Room';
import { Feature } from './entities/Feature';
import { Location } from './entities/Location';
import { ScheduleItem } from './entities/ScheduleItem';
import { Schedule } from './entities/Schedule';
import { Student } from './entities/Student';
import { Dashboard } from './components/dashboard/Dashboard';
import { Header } from './components/header/Header';

function App() {
  var feature = { icon_path: logo, name: "Number of Seats", quantity: 6 } as Feature;
  var features = [ feature, feature, feature, feature];
  var location = { id: 1, name: "TestLocation", rooms: [1] } as Location;
  var room = { name: "TestRoom", id: 1, location, features: features, image_url: meeting_room, size: "small" } as Room;
  var now = new Date();
  var now_plus_1_hour = new Date(now.getTime() + 60 * 60 * 1000);
  var now_plus_2_hours = new Date(now.getTime() + 2 * 60 * 60 * 1000);
  var tomorrow = new Date(now.getTime() + 24 * 60 * 60 * 1000);
  var tomorrow_plus_1_hour = new Date(tomorrow.getTime() + 60 * 60 * 1000);
  var schedule_item = { room: room, startDate: now_plus_1_hour, endDate: now_plus_2_hours } as ScheduleItem;
  var schedule_item_tomorrow = { room: room, startDate: tomorrow, endDate: tomorrow_plus_1_hour } as ScheduleItem;
  var schedule_items = [schedule_item, schedule_item, schedule_item, schedule_item, schedule_item, schedule_item, schedule_item_tomorrow, schedule_item_tomorrow];
  var schedule = { items: schedule_items } as Schedule;
  var student = { schedule: schedule, firstName: "Taylor", lastName: "Jarvis", credits: 5, id: 1  } as Student;

  return (
    <div>
      <Header {...student} />
      <Dashboard {...student} />
    </div>
  );
}

export default App;
