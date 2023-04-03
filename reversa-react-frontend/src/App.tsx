import React from 'react';
import logo from './assets/logo.svg';
import meeting_room from "./assets/meeting_room.jpg"

import { Room } from './entities/Room';
import { Feature } from './entities/Feature';
import { Location } from './entities/Location';
import { ScheduleItem } from './entities/ScheduleItem';
import { Schedule } from './entities/Schedule';
import { Student } from './entities/Student';
import { Header } from './components/header/Header';
import { RoomTable } from './components/room/RoomTable';


function App() {
  var feature = { icon_path: logo, name: "Number of Seats", quantity: 6 } as Feature;
  var features = [ feature, feature, feature, feature];
  var location = { id: 1, name: "TestLocation", rooms: [1] } as Location;
  var room = { name: "TestRoom", id: 1, location, features: features, image_url: meeting_room, size: "small" } as Room;

  var schedule_item = { room: room, startDate: new Date() } as ScheduleItem;
  var schedule = { items: [schedule_item, schedule_item, schedule_item, schedule_item] } as Schedule;
  var student = { schedule: schedule, firstName: "Taylor", lastName: "Jarvis", credits: 5, id: 1  } as Student;


  return (
    <div>
      <Header {...student} />
      <RoomTable data = {[room, room, room]}/> 
    </div>
  );
}

export default App;
