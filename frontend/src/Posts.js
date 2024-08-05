// Posts.js

import React, {Component} from "react";
import PostService from "./PostService";

const postService = new PostService();

export default class Posts extends Component {
    constructor(props){
        super(props)
        this.state = {
            data : [],
            inputValue: ''
        }

        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleChange(event) {
        this.setState({inputValue: event.target.value});
    }

handleSubmit(event) {
    event.preventDefault(); // Prevent default form submission
    postService.createPost({'text' : this.state.inputValue}).then(() => {
        this.getData(); // Refresh the data after submission
        this.setState({inputValue : ''});
    });
}

handleKeyPress(event) {
    if (event.key === 'Enter') {
        this.handleSubmit(event);
    }
}

    getData(){
        postService.getPosts().then(result => {
            this.setState({data: result.data})
        })
    }

    componentDidMount(){
        this.getData()
    }

    setLike(post) {
        postService.setLikePost(post.id)
        post.likesCount += 1
        this.forceUpdate()
    }

deletePost(postId) {
    postService.deletePost(postId).then(() => {
        this.getData(); // Refresh the data after deletion
    });
}

render() {
    return (
        <div id='posts'>
            {this.state.data.map(post =>
                <div id={'post_' + post.id} key={post.id}>
                    <p>{post.text}</p>
                    <button onClick={() => this.setLike(post)}>{post.likesCount}</button>
                    <button onClick={() => this.deletePost(post.id)}>Delete</button>
                    <p>Date: {post.date}</p>
                    <hr />
                </div>
            )}
            <input type='text' onChange={this.handleChange} onKeyPress={(e) => this.handleKeyPress(e)} value={this.state.inputValue} />
            <button onClick={this.handleSubmit}>Send</button>
        </div>
    );
}

}
