import React from 'react';
import logo from './assets/logo.svg';
import meeting_room from "./assets/meeting_room.jpg"

import { Room } from './entities/Room';
import { Feature } from './entities/Feature';
import { Location } from './entities/Location';
import { Details } from './components/room/Details';

function App() {
  var feature = { icon_path: logo, name: "Number of Seats", quantity: 6 } as Feature;
  var features = [ feature, feature, feature, feature];
  var location = { id: 1, name: "TestLocation", rooms: [1] } as Location;
  var room = { name: "TestRoom", id: 1, location, features: features, image_url: meeting_room, size: "small" } as Room;


  return (
    <div>
      <Details {...room} />
    </div>
  );
}

export default App;
