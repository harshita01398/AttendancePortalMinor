import React from 'react';
import Loading from './Loading';

class ButtonGroup extends React.Component{
    constructor(props){
        super(props);
        this.state = { file: '', loading: false };
        this.uploadFile = this.uploadFile.bind(this);
        this.reader = new FileReader();
    }

    uploadFile(e){
        this.reader.readAsDataURL(e.target.files[0]);
    }

    componentDidMount(){
        this.reader.onload = () => {
            this.setState({ file: this.reader.result });
        };
        this.reader.onloadstart = () => {
            this.setState({ loading: true });
        };
        this.reader.onprogress = (data) => {
            this.setState({ loading: data.loaded/data.total*100 });
        };
        this.reader.onloadend = () => {
            this.setState({ loading: false });
        };
    }

    render(){
        return(
            <div className='container'>
            {
                this.state.loading ? <Loading progress={this.state.loading}/> :
        <div>
        <input type='file' accept={'image/*'} onChange={this.uploadFile}/>
        <img src={this.state.file}/>
        <button disabled={!this.state.file}> Convert </button>
        </div>
    }
    </div>
    );
    }
}

export default ButtonGroup;