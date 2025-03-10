import React, { Component, Fragment } from 'react';
import { withStyles } from '@material-ui/core/styles';
import Typography from '@material-ui/core/Typography';

const styles = theme => ({
    text: {
        padding: theme.spacing(2, 2, 0),
        textTransform: "uppercase"
    },
    paper: {
        paddingBottom: 50,
    },
    root: {
        display: 'flex',
        flexWrap: 'wrap',
        '& > *': {
            margin: theme.spacing(1),
            width: theme.spacing(16),
            height: theme.spacing(16),
        },
    },
});


class Contact extends Component {

    render() {
        const { classes } = this.props;

        return (
            <Fragment>
                <div className={classes.root}>
                    <Typography className={classes.text} variant="h5" gutterBottom>
                        Contact Me
                    </Typography>
                </div>
            </Fragment>
        );
    }
}

export default withStyles(styles)(Contact);