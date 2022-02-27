FROM node



ARG FUNCTION_DIR="/var/task"



RUN mkdir -p ${FUNCTION_DIR}



COPY src ${FUNCTION_DIR}/src



RUN npm install



RUN npm install dynamodb-doc



CMD [ "/var/task/src/GenerateTallyDataJSON.handler" ]
