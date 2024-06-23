import { BottomNavigation, BottomNavigationAction, Paper } from "@mui/material";
import { useNavigate } from "react-router-dom";

// Icon names found at: https://fonts.google.com/icons
import { Place as NearbyIcon } from '@mui/icons-material';
import { Map as MapIcon } from '@mui/icons-material';
import { ListAlt as ListIcon } from '@mui/icons-material';
import { Settings as SettingsIcon } from '@mui/icons-material';

export function NavBar() {
    let navigate = useNavigate();

    return (
    <>
    <Paper sx={{ position: 'fixed', bottom: 0, left: 0, right: 0 }} elevation={3}>
    <BottomNavigation showLabels>
        <BottomNavigationAction label="Nearby" icon={<NearbyIcon />} onClick={ () => navigate("/")}/>
        <BottomNavigationAction label="Map" icon={<MapIcon />} onClick={() => navigate("/map")} />
        <BottomNavigationAction label="ViewAll" icon={<ListIcon />} onClick={() => navigate("/list")} />
        <BottomNavigationAction label="Settings" icon={<SettingsIcon />} onClick={() => navigate("/settings")} />
    </BottomNavigation>
    </Paper>
    </>
    );
}

export default NavBar;