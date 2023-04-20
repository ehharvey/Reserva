import { RouterProvider, createBrowserRouter } from "react-router-dom";
import { Root } from "./routes/Root";
import { Profile } from "./routes/Profile";
import { Groups } from "./routes/Groups";
import { AppHeader } from "./components/header/AppHeader";
import { Auth0Provider } from "@auth0/auth0-react";
import { Rooms } from "./routes/Rooms";
import { BookingForm } from "./routes/BookingForm";

const router = createBrowserRouter([
  {
    path: "/",
    element: <Root />,
  },
  {
    path: "/me",
    element: <Profile />
  }, 
  {
    path: "/rooms",
    element: <Rooms />
  },
  {
    path: "/groups",
    element: <Groups />
  },
  {
    path: "/booking-request/:roomId",
    element: <BookingForm />
  }
]);

export function App() {
  return (
    <Auth0Provider
      domain="" // TODO: Add your Auth0 domain
      clientId="" // TODO: Add your Auth0 client ID
      authorizationParams={{
        redirect_uri: window.location.origin
      }}
    >
      <AppHeader />
      <RouterProvider router={router} />
    </Auth0Provider>
  )
}