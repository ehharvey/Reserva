import { RouterProvider, createBrowserRouter } from "react-router-dom";
import { Profile } from "./routes/Profile";
import { Root } from "./routes/Root";
import { AppHeader } from "./components/header/AppHeader";
import { Auth0Provider } from "@auth0/auth0-react";

const router = createBrowserRouter([
  {
    path: "/",
    element: <Root />,
  },
  {
    path: "/me",
    element: <Profile />
  }
]);

export function App() {
  return (
    <Auth0Provider
      domain={import.meta.env.VITE_AUTH_DOMAIN}
      clientId={import.meta.env.VITE_AUTH_CLIENT_ID}
      authorizationParams={{
        redirect_uri: window.location.origin
      }}
    >
      <AppHeader />
      <RouterProvider router={router} />
    </Auth0Provider>
  )
}