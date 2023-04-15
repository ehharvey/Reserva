import { Button, Group } from "@mantine/core";
import { useAuth0 } from "@auth0/auth0-react";
import { User } from "../../entities/User";



export function AuthButtons() {
    const { logout, isAuthenticated, user, loginWithPopup } = useAuth0();

    return (
        <Group position="center" grow pb="xl" px="md">
            {isAuthenticated ? (
                <>
                    Hello, {user?.name}!
                    <Button variant="default" onClick={() => { logout({ logoutParams: { returnTo: window.location.origin } }) }}>Log out</Button>
                </>
            ) : (
                <>
                    <Button variant="default" onClick={() => { loginWithPopup() }}>Log in</Button>
                    <Button>Sign up</Button>
                </>
            )}
        </Group>
    )
}