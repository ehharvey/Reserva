import { Button, Group } from "@mantine/core";
import { RedirectLoginOptions, useAuth0 } from "@auth0/auth0-react";
import { ConfigContext } from "../../contexts/ConfigProvider";
import { useContext } from "react";

export function AuthButtons() {
    const { logout, isAuthenticated, user, loginWithRedirect } = useAuth0();
    const config = useContext(ConfigContext);

    var standardLoginOptions = {
        redirectUri: window.location.origin,
        audience: config?.api.baseUrl,
        scope: `
            read:groups:associated
            read:unavailabilities:me
            write:groupmemberships:me
            write:groups:me
            write:unavailabilities:me
        `,
    } as RedirectLoginOptions;

    var adminLoginOptions = {
        redirectUri: window.location.origin,
        audience: config?.api.baseUrl,
        scope: `
            read:items:me
            read:unavailabilities:me
            write:items:me
            write:unavailabilities:me
            read:items
            write:items
        `,
    } as RedirectLoginOptions;

    return (
        <Group position="center">
            {isAuthenticated ? (
                <>
                    Hello, {user?.name}!
                    <Button variant="default" onClick={() => { logout({ logoutParams: { returnTo: window.location.origin } }) }}>Log out</Button>
                </>
            ) : (
                <>
                    <Button variant="default" onClick={() => { loginWithRedirect(standardLoginOptions) }}>Login</Button>
                </>
            )}
        </Group>
    )
}