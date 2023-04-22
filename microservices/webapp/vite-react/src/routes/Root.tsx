import { useState } from 'react'
import reservaLogo from '../assets/reserva.png'
import { Button } from '@mantine/core'
import './Root.css'

export function Root() {
    // const [count, setCount] = useState(0)

  return (
    <div>
      <div>
        <a> 
          <img src= {reservaLogo} className="logo reserva" alt="Reserva logo" />
        </a>
      </div>
      <h1>Welcome to Reserva!</h1>
      <p> 
        Our study room booking system provides easy access to booking study rooms on campus.
        <br></br>
        Our system is user-friendly and designed to make your study experience stress-free. 
        <br></br>
        Start booking your study room today and elevate your academic success! 
      </p>
    </div>
  )
}