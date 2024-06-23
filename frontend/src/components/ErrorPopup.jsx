import { Paper, Button} from '@mui/material';
import { useError } from '../contexts/ErrorContext';

export function ErrorPopup() {
    const { error, clearError } = useError();

    if (!error) {
        return null;
    }

    return (
        <>
        <Paper elevation={3} className="w-96 h-96 bg-white">
            <h1 className="text-4xl text-center pt-10">Error</h1>
            <p className="text-center"> {error} </p>

            <Button variant="contained" onClick={clearError}>
                Close
            </Button>
        </Paper>
        </>
    );
}