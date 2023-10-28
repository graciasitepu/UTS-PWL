import Spinner from 'react-bootstrap/Spinner';

function LoadingSpinner() { // spinner loading saat proses data 
    return (
        <Spinner animation="border" role="status">
         <span className="visually-hidden">Loading...</span>
        </Spinner>
    );
}

export default LoadingSpinner;