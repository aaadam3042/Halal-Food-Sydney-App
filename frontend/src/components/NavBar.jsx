import { BottomNavigation, BottomNavigationAction, Box, styled } from "@mui/material";
import { useNavigate } from "react-router-dom";

// Icon names found at: https://mui.com/material-ui/material-icons/
import { Place as NearbyIcon } from '@mui/icons-material';
import { Map as MapIcon } from '@mui/icons-material';
import { ListAlt as ListIcon } from '@mui/icons-material';
import { Settings as SettingsIcon } from '@mui/icons-material';
import { useState } from "react";

export function NavBar() {
    let navigate = useNavigate();
    const [value, setValue] = useState(0);
    const Offset = styled('div')(({ theme }) => theme.mixins.toolbar);

    return (
    <>
    <Box sx={{ position: 'fixed', bottom: 0, left: 0, right: 0}} >
    <BottomNavigation showLabels value={value} onChange={(event, newValue) => {
      setValue(newValue);
    }}>
        <BottomNavigationAction label="Nearby" icon={<NearbyIcon fontSize="large"/>} onClick={ () => navigate("/")}/>
        <BottomNavigationAction label="Map" icon={<MapIcon  fontSize="large"/>} onClick={() => navigate("/map")} />
        <BottomNavigationAction label="ViewAll" icon={<ListIcon  fontSize="large"/>} onClick={() => navigate("/list")} />
        <BottomNavigationAction label="Settings" icon={<SettingsIcon  fontSize="large"/>} onClick={() => navigate("/settings")} />
    </BottomNavigation>
    </Box>
    <Offset />
    </>
    );
}

export default NavBar;