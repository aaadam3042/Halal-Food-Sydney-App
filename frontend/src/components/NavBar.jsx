import { BottomNavigation, BottomNavigationAction, Paper } from "@mui/material";

import { Place as NearbyIcon } from '@mui/icons-material';
import { Map as MapIcon } from '@mui/icons-material';
import { ListAlt as ListIcon } from '@mui/icons-material';
import { Settings as SettingsIcon } from '@mui/icons-material';

export function NavBar() {
    return (
    <>
    <Paper sx={{ position: 'fixed', bottom: 0, left: 0, right: 0 }} elevation={3}>
    <BottomNavigation showLabels>
        <BottomNavigationAction label="Nearby" icon={<NearbyIcon />} />
        <BottomNavigationAction label="Map" icon={<MapIcon />} />
        <BottomNavigationAction label="ViewAll" icon={<ListIcon />} />
        <BottomNavigationAction label="Settings" icon={<SettingsIcon />} />
    </BottomNavigation>
    </Paper>
    </>
    );
}

export default NavBar;