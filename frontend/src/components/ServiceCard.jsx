import { Box, Paper, Stack, Typography } from "@mui/material";
import ServiceSummaryCard from "./ServiceSummaryCard";

export function ServiceCard({title, services}) {
    const servicesList = services.map(service =>
        <>
        <ServiceSummaryCard key={service.id} service={service} padding={1} margin={2} />
        </>
    )
    
    return (
    <>
    <Paper elevation={3} sx={{borderRadius: 2.5, backgroundColor: "#a0998e", margin: "15px 0 15px 0"}}>  {/* Instead of doing border colour the cards should be elevated and padded apart */}
        <Stack>
            <Paper elevation={4} square sx={{backgroundImage: "", borderRadius: "10px 10px 0 0"}}>
                <Typography>
                    {title}
                </Typography>
            </Paper>

            {servicesList}

            <Paper elevation={3} sx={{backgroundColor: "#715e55", borderRadius: "0 0 10px 10px"}}>
                <Typography>
                    More {title.toLowerCase()} nearby
                </Typography>
            </Paper>
        </Stack>
    </Paper>
    </>
    );
}

export default ServiceCard;