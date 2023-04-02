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
import { BookingPage } from './components/booking/BookingPage';
import { Group } from './entities/Group';

function App() {
  var feature = { icon_path: logo, name: "Number of Seats", quantity: 6 } as Feature;
  var features = [ feature, feature, feature, feature];
  var location = { id: 1, name: "TestLocation", rooms: [1] } as Location;
  var room = { name: "TestRoom", id: 1, location, features: features, image_url: meeting_room, size: "small" } as Room;

  var schedule_item = { room: room, startDate: new Date() } as ScheduleItem;
  var schedule = { items: [schedule_item, schedule_item, schedule_item, schedule_item] } as Schedule;
  var student = { schedule: schedule, firstName: "Taylor", lastName: "Jarvis", credits: 5, id: 1  } as Student;

  var group1 = { id: 1, name: "Project 6", created_by: 1, member: ["Studnet A", "Studnet B"]} as Group;
  var group2 = { id: 2, name: "Enterprise", created_by: 1, member: ["Studnet A", "Studnet C"]} as Group;
  var group3 = { id: 3, name: "SQ4", created_by: 1, member: ["Studnet A", "Studnet D"]} as Group;
  var myGroups = [ group1, group2, group3 ] as Group[];
  
  return (
    <div>
      <Header {...student} />
      <BookingPage groups={myGroups} />
    </div>
  );
}

export default App;
