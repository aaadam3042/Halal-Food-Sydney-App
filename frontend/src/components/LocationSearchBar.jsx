import { AppBar, Box, Toolbar, Typography, styled } from "@mui/material";

// Icons
import { Search as SearchIcon } from '@mui/icons-material';
import { NearMe as LocationIcon } from '@mui/icons-material';

export function LocationSearchBar() {
    const Offset = styled('div')(({ theme }) => theme.mixins.toolbar);
    return (
    <>
    <AppBar sx={{top: 60, left: 0, right: 0, width: '100%', backgroundColor: "brown"}} position="fixed">
        <Toolbar>
        <Box paddingX={1} paddingY={0} sx={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', width: '100%' }}>
            <Typography variant="h6" component="div" sx={{ flexGrow: 1, textAlign: "left" }} margin={0} padding={0}>
                Lakemba, NSW
            </Typography>
            <Box>
            <SearchIcon sx={{fontSize: 28, marginRight:2}} />
            <LocationIcon sx={{fontSize: 28, marginRight:2}} />
            </Box>
        </Box>
        </Toolbar>
    </AppBar>
    <Offset />
    </>
    );
}

export default LocationSearchBar;