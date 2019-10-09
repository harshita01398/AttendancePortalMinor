import React from 'react';
const Loading = (props) => {
    return(
        <div className="loading">
            <h1> Loading .. {Math.round(props.progress)} % </h1>
        </div>
    );
};

export default Loading;