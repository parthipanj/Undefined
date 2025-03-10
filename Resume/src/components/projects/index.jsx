import React, { Component, Fragment } from 'react';
import { withStyles } from '@material-ui/core/styles';
import Container from '@material-ui/core/Container';
import Typography from '@material-ui/core/Typography';
import Divider from '@material-ui/core/Divider';
import Card from '@material-ui/core/Card';
import CardContent from '@material-ui/core/CardContent';
import List from '@material-ui/core/List';
import ListItem from '@material-ui/core/ListItem';
import Box from '@material-ui/core/Box';
import Paper from '@material-ui/core/Paper';
import Chip from '@material-ui/core/Chip';
import { projects } from '../../static/json/projects';

const styles = theme => ({
    root: {
        flexGrow: 1,
        backgroundColor: 'white',
    },
    text: {
        padding: theme.spacing(3, 0, 3),
        textTransform: "uppercase",
        textAlign: 'center',
    },
    gridItem: {
        margin: 'auto',
        width: 850,
        height: '100%',
        maxWidth: '100%',
        maxHeight: '100%',
    },
    cardRoot: {
        display: 'flex',
        width: '100%',
    },
    details: {
        display: 'flex',
        flexDirection: 'column',
        textAlign: 'end',
        width: '50%',
    },
    cardContent: {
        width: '50%',
    },
    paper: {
        display: 'flex',
        justifyContent: 'center',
        flexWrap: 'wrap',
        listStyle: 'none',
        padding: theme.spacing(0.5),
        margin: 0,
    },
    chip: {
        margin: theme.spacing(0.5),
    },
});

class Projects extends Component {

    render() {
        const { classes } = this.props;

        return (
            <Fragment>
                <Container className={classes.root}>
                    <Typography className={classes.text} variant="h5">
                        Projects
                    </Typography>
                </Container>
                <Container className={classes.root}>
                    <List>
                        {projects.map((project, index) => {
                            return (
                                <ListItem key={index} className={classes.gridItem}>
                                    <Card className={classes.cardRoot} elevation={0}>
                                        <CardContent border={0} className={classes.details}>
                                            <Typography component='h6' variant='h6'>{project.name}</Typography>
                                        </CardContent>
                                        <Divider orientation='vertical' flexItem />
                                        <CardContent border={0} className={classes.cardContent}>
                                            <Typography variant='subtitle2' color='textSecondary'>{project.description}</Typography>
                                            <Paper elevation={0} component="ul" className={classes.paper}>
                                                {project.keywords.map((keyword, key) => {
                                                    return (
                                                        <Box component='li' key={key}>
                                                            <Chip label={keyword} className={classes.chip}/>
                                                        </Box>
                                                    )
                                                })}
                                            </Paper>
                                        </CardContent>
                                    </Card>
                                </ListItem>
                            )
                        })}
                    </List>
                </Container>
            </Fragment >
        );
    }
}

export default withStyles(styles)(Projects);