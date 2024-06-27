import { Box, Paper, Typography } from "@mui/material";

export function ServiceSummaryCard({service, padding, margin}) {
    return(
    <>
    <Box margin={`${margin}px 0px ${margin}px 0px`}>
    <Paper bgcolor="#a0998e" elevation={5} sx={{backgroundColor: "#a0998e"}}>
        <Box padding={padding}>
            <Typography>
                {service.name}
            </Typography>
            <Typography>
                {service.distance} - {service.openTime}
            </Typography>
            <Typography>
                {service.contact}
            </Typography>
            <Typography>
                {service.halalStatus}
            </Typography>
        </Box>
    </Paper>
    </Box>
    </>
    );
}

export default ServiceSummaryCard;