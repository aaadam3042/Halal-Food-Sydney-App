import { Box, Paper, Typography } from "@mui/material";

// Icons
import { Search as SearchIcon } from '@mui/icons-material';
import { NearMe as LocationIcon } from '@mui/icons-material';

export function LocationSearchBar() {
    return (
    <>
    <Paper square sx={{ position: 'fixed', top: 70, left: 0, right: 0, width: '100%'}}>
        <Box paddingX={4} paddingY={0.5} sx={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', width: '100%' }}>
            <Typography variant="h5" component="div" padding={2} sx={{ flexGrow: 1 }}>
                Lakemba, NSW
            </Typography>
            <Box>
            <SearchIcon fontSize="large" />
            <LocationIcon fontSize="large" />
            </Box>
        </Box>
    </Paper>
    </>
    );
}

export default LocationSearchBar;