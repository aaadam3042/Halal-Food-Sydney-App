import { AppBar, Box, Button, Toolbar, Typography, styled } from '@mui/material';

export function Header() {
    const Offset = styled('div')(({ theme }) => theme.mixins.toolbar);
    return(
    <>
        <Box sx={{flexGrow: 1}}>
            <AppBar position="fixed">
                <Toolbar>
                <Typography variant="h5" component="div" padding={2} sx={{ flexGrow: 1 }}>
                    Halal Food Sydney 
                </Typography>
                <Button> login </Button>
                </Toolbar>
            </AppBar>
            <Offset />
        </Box>
    </>
    );
}

export default Header;