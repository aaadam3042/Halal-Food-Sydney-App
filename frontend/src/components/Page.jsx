import {Box} from '@mui/material'

export function Page({margin, topMargin, bottomMargin}) {
    return(
    <>
    <Box margin={`${margin}px 0 ${margin}px 0 `} marginTop={topMargin} marginBottom={bottomMargin}>
        {}
    </Box>
    </>
    );
}

export default Page;