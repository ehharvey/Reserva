import { Button, Group } from "@mantine/core";
import { useAuth0 } from "@auth0/auth0-react";
import { User } from "../../entities/User";
import { useEffect, useState } from "react";
import { GroupApi, Configuration, GroupsPostRequest } from "../../fetch";



export function AuthButtons() {
    const { logout, isAuthenticated, user, loginWithRedirect, getAccessTokenSilently, getAccessTokenWithPopup } = useAuth0();
    const [test, setTest] = useState<string | null>(null);

    var loginOptions = {
        redirectUri: window.location.origin,
        audience: "http://localhost:8080",
        scope: "openid profile email",
    };

    useEffect(() => {
        if (isAuthenticated) {
            getAccessTokenWithPopup({ authorizationParams: {
                audience: "http://localhost:8080",
                scope: "write:groups:me"
            }}).then((token) => {
                console.log(token);

                var config = new Configuration({
                    basePath: "http://localhost:8080", accessToken: "Bearer " + token, 
                });
                
                var foo = new GroupApi(config);
    
                var request = {
                    newGroup: {
                        name: "test",
                        createdBy: "user-28e5e6f6-de0a-45ce-bc12-54d3810a99b1",
                    }
                } as GroupsPostRequest;
    
                foo.groupsPost(request).then((response) => {
                    console.log(response);
                });
            });

            
        }
    }, [isAuthenticated]);

    return (
        <Group position="center" grow pb="xl" px="md">
            {isAuthenticated ? (
                <>
                    Hello, {user?.name}!
                    <Button variant="default" onClick={() => { logout({ logoutParams: { returnTo: window.location.origin } }) }}>Log out</Button>
                </>
            ) : (
                <>
                    <Button variant="default" onClick={() => { loginWithRedirect() }}>Log in</Button>
                    <Button>Sign up</Button>
                </>
            )}
        </Group>
    )
}