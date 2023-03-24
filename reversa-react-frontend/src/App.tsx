import React from 'react';
import logo from './assets/logo.svg';
import meeting_room from "./assets/meeting_room.jpg"

import { Room } from './entities/Room';
import { Feature } from './entities/Feature';
import { Location } from './entities/Location';
import { Details } from './components/room/Details';
import { ScheduleItem } from './entities/ScheduleItem';
import { Schedule } from './entities/Schedule';
import { Student } from './entities/Student';
import { Dashboard } from './components/dashboard/Dashboard';

function App() {
  var feature = { icon_path: logo, name: "Number of Seats", quantity: 6 } as Feature;
  var features = [ feature, feature, feature, feature];
  var location = { id: 1, name: "TestLocation", rooms: [1] } as Location;
  var room = { name: "TestRoom", id: 1, location, features: features, image_url: meeting_room, size: "small" } as Room;

  var schedule_item = { room: room, datetime: new Date() } as ScheduleItem;
  var schedule = { items: [schedule_item, schedule_item, schedule_item, schedule_item] } as Schedule;
  var student = { schedule: schedule, firstName: "Taylor", lastName: "Jarvis", credits: 5, id: 1  } as Student;

  return (
    <div className="container">
      <Dashboard {...student} />
    </div>
  );
}

export default App;
