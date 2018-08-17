matrix = require("matrix")

local dh = {
	{100,10},
	{50,30},
	{100,10},
}

function love.load()
end

function jacobian(dh)
	local j = {}

	local sx = 0
	local sy = 0
	for i=1,table.getn(dh) do
		local row = dh[table.getn(dh)-i+1]
		local d = row[1]
		local theta = row[2]
		sx = sx-d*math.sin(theta)
		sy = sy+d*math.cos(theta)
		table.insert(j,{sx,sy})
	end

	local jj = {}
	for i,row in pairs(j) do
		table.insert(jj,j[table.getn(dh)-i+1])
	end

	return matrix.transpose(jj)
end

function forward_kinematics(dh)
	local X = {}
	local x1=0
	local y1=0
	for i,row in pairs(dh) do
		local d = row[1]
		local theta = row[2]
		x1 = x1 + d*math.cos(theta)
		y1 = y1 + d*math.sin(theta)
	end

	return {{x1},{y1}}
end

function inverse_kinematics(dh,mouse)
	local j = jacobian(dh)
	local jt = matrix.transpose(j)
	local X = forward_kinematics(dh)
	return matrix.mul(jt,matrix.sub(X,mouse))
end

function love.draw()
	love.graphics.translate(love.graphics.getWidth()/2,love.graphics.getHeight()/2)

	local mouse = {{love.mouse.getX() - love.graphics.getWidth()/2},{love.mouse.getY()- love.graphics.getHeight()/2}}
	local delta = inverse_kinematics(dh,mouse)

	-- update dh
	for i,row in pairs(dh) do
		dh[i][2] =  dh[i][2] - delta[i][1]*0.00001
	end

	local x1=0
	local y1=0
	local x2,y2
	for i,row in pairs(dh) do
		local d = row[1]
		local theta = row[2]
		x2 = x1+d*math.cos(theta)
		y2 = y1+d*math.sin(theta)
		love.graphics.setColor(1,1,1,1)
		love.graphics.line(x1,y1,x2,y2)
		x1 = x2
		y1 = y2
	end

end

