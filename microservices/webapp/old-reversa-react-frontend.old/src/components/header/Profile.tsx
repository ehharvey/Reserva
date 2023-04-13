import { useState } from "react";
import { Image } from "react-bootstrap";
import Offcanvas from "react-bootstrap/esm/Offcanvas";
import profile from "../../assets/profile.png";
import { Login } from "../login/Login";

export function Profile() {
    const [show, setShow] = useState(false);

    const handleClose = () => setShow(false);
    const handleShow = () => setShow(true);

    var loginProps = { onLogin: (username: string, password: string) => { console.log(username + ":" + password) } };

    return (
        <>
            <Image role={"button"} src={profile} onClick={handleShow} roundedCircle width="30" height="30" className="ml-2" />

            <Offcanvas placement="end" show={show} onHide={handleClose}>
                <Offcanvas.Body>
                    <Login {...loginProps} />
                </Offcanvas.Body>
            </Offcanvas>
        </>
    );
}