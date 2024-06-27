import { AppBar, Box, Toolbar, Typography, styled } from "@mui/material";

// Icons
import { Search as SearchIcon } from '@mui/icons-material';
import { NearMe as LocationIcon } from '@mui/icons-material';

export function LocationSearchBar() {
    const Offset = styled('div')(({ theme }) => theme.mixins.toolbar);
    return (
    <>
    <AppBar square sx={{top: 70, left: 0, right: 0, width: '100%', backgroundColor: "brown"}} position="fixed">
        <Toolbar>
        <Box paddingX={4} paddingY={0.5} sx={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', width: '100%' }}>
            <Typography variant="h5" component="div" padding={2} sx={{ flexGrow: 1 }}>
                Lakemba, NSW
            </Typography>
            <Box>
            <SearchIcon fontSize="large" />
            <LocationIcon fontSize="large" />
            </Box>
        </Box>
        </Toolbar>
    </AppBar>
    <Offset />
    </>
    );
}

export default LocationSearchBar;