import { useEffect, useState } from 'react';
import ReservaLogo from '../../assets/ReservaLogo.png';

import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import { Image } from 'react-bootstrap';
import { CreditSummary } from './CreditSummary';
import { Student } from '../../entities/Student';
import { Profile } from './Profile';

export function Header(student: Student) {
    const [currentTime, setCurrentTime] = useState(new Date());

    useEffect(() => {
        const interval = setInterval(() => setCurrentTime(new Date()), 100);
        return () => {
            clearInterval(interval);
        };
    }, []);

    return (
        <Navbar>
            <Container fluid>
                <Navbar.Brand href="#home">
                    <Image height="30" width="30" src={ReservaLogo} />
                    &nbsp;
                    Reserva
                </Navbar.Brand>
                <Navbar.Collapse className="justify-content-end">  
                    <Nav className="me-auto">
                        <Nav.Link href="#rooms">Rooms</Nav.Link>
                        <Nav.Link href="#groups">Groups</Nav.Link>
                    </Nav>
                    <Navbar.Text>
                        <CreditSummary {...student} />
                    </Navbar.Text>
                    <Navbar.Text>
                        {currentTime.toLocaleDateString()}
                        &nbsp;
                        {currentTime.toLocaleTimeString()}
                    </Navbar.Text>
                    <Profile />
                </Navbar.Collapse>
            </Container>
        </Navbar>    
    )
}