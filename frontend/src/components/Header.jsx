import { AppBar, Typography } from '@mui/material';

export function Header() {
    return(
    <>
        <AppBar position="fixed">
            <Typography variant="h4" component="div" padding={2} sx={{ flexGrow: 1 }}>
                Halal Food Sydney 
            </Typography>
        </AppBar>
    </>
    );
}

export default Header;