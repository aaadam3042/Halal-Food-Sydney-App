import { Box, Paper, Stack, Typography } from "@mui/material";
import ServiceSummaryCard from "./ServiceSummaryCard";

import {KeyboardArrowRight as RightArrowIcon} from '@mui/icons-material';
import {KeyboardDoubleArrowRight as DoubleRightArrowIcon} from "@mui/icons-material";

export function ServiceCard({title, services, banner}) {
    const servicesList = services.map(service =>
        <>
        <ServiceSummaryCard key={service.id} service={service} padding={1} margin={2} />
        </>
    )
    
    return (
    <>
    <Paper elevation={3} sx={{borderRadius: 2.5, backgroundColor: "#a0998e", margin: "15px 0 15px 0", width: "400px"}} >
        <Stack>
            <Paper elevation={4} square sx={{borderRadius: "10px 10px 0 0", alignContent: "center", position: "relative", height: 40, backgroundColor: "transparent", marginBottom: 0.5}}>
                <Box position="absolute" top="0px" bottom="0px" left="0px" right="0px" zIndex={1} borderRadius="10px 10px 0 0" style={{backgroundImage:`url(${banner})`, backgroundSize: "cover", height: 40, filter: "blur(1px)"}} />
                <Stack direction="row" justifyContent="space-between">
                    <Typography alignContent="center" paddingLeft={2} color="white" fontWeight="bolder" zIndex={3}>
                        {title} 
                    </Typography>
                    <DoubleRightArrowIcon fontSize="large" sx={{zIndex: 3}}/>
                </Stack>
            </Paper>   

            {servicesList}

            <Paper elevation={3} sx={{backgroundColor: "#715e55", borderRadius: "0 0 10px 10px", height: 40, marginTop: 0.5, alignContent: "center"}}>
                <Stack direction="row" justifyContent="space-between">
                <Typography color="white" fontWeight="bold" fontSize={15} alignContent="center" paddingLeft={2}>
                    More {title.toLowerCase()} nearby
                </Typography>
                <RightArrowIcon fontSize="large" />
                </Stack>
            </Paper>
        </Stack>
    </Paper>
    </>
    );
}

export default ServiceCard;