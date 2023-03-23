import React from 'react';
import { render, screen } from '@testing-library/react';
import { Details } from '../Details';
import { Feature } from '../../../entities/Feature';
import { Location } from '../../../entities/Location';
import { Room } from '../../../entities/Room';
import logo from '../../../assets/logo.svg';
import meeting_room from '../../../assets/meeting_room.jpg';


var feature = { icon_path: logo, name: "Number of Seats", quantity: 6 } as Feature;
  var features = [ feature, feature, feature, feature];
  var location = { id: 1, name: "TestLocation", rooms: [1] } as Location;
  var room = { name: "TestRoom", id: 1, location, features: features, image_url: meeting_room, size: "small" } as Room;



test('Basic Details test', () => {
    render(<Details {...room} />);
    const linkElement = screen.getByText("TestRoom");
    expect(linkElement).toBeInTheDocument();
  });