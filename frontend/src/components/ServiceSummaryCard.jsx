import { Box, Paper, Stack, Typography } from "@mui/material";
import {KeyboardArrowRight as RightArrowIcon} from '@mui/icons-material';

export function ServiceSummaryCard({service, padding, margin}) {
    let metaline1 = `${service.distance}km `
    if (service.openTime) {
        metaline1 += `| ${service.openTime}`
    }
    let metaline2 = `${service.phone} `
    if (service.email) {
        metaline2 += `| ${service.email}`
    }

    return(
    <>
    <Box margin={`${margin}px 0px ${margin}px 0px`}>
    <Paper bgcolor="#a0998e" elevation={5} sx={{backgroundColor: "#a0998e"}}>
        <Stack direction="row" justifyContent="space-between">
        <Box padding={padding} paddingLeft={2} textAlign="start">
            <Typography fontSize={20} fontWeight="bolder" color="#413528">
                {service.name}
            </Typography>
            <Typography color="lightgray">
                {metaline1}
            </Typography>
            <Typography color="lightgray">
                {metaline2}
            </Typography>
            <Box borderRadius={3} bgcolor="lightblue" alignContent="center" textAlign="center" width={130}>
                <Typography fontSize={13}>
                    {service.halalStatus}
                </Typography>
            </Box>
        </Box>
        <RightArrowIcon sx={{fontSize: 70, alignSelf: "center"}} />
        </Stack>
    </Paper>
    </Box>
    </>
    );
}

export default ServiceSummaryCard;